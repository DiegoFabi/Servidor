-- Aura Sombría (custom): anillo de almas girando alrededor del élite mientras
-- está en combate; quien se acerque a 3 bloques recibe Oscuridad un instante.
local function ring(context, center, radius, offset, particle)
  for i = 0, 11 do
    local a = offset + (i * math.pi / 6)
    context.world:spawn_particle_at_location(em.create_location(
      center.x + math.cos(a) * radius, center.y + 0.2, center.z + math.sin(a) * radius, center.world
    ), { particle = particle, amount = 1, x = 0, y = 0, z = 0, speed = 0 }, 1)
  end
end

return {
  api_version = 1,
  on_enter_combat = function(context)
    if not context.cooldowns:local_ready("aura_sombria") then
      return
    end
    context.cooldowns:set_local(600, "aura_sombria")
    local ticks = 0
    local task
    task = context.scheduler:run_every(4, function()
      ticks = ticks + 4
      if ticks > 600 or not context.boss:is_alive() then
        context.scheduler:cancel_task(task)
        return
      end
      local loc = context.boss:get_location()
      ring(context, loc, 1.1, ticks / 10, "SOUL_FIRE_FLAME")
      ring(context, loc, 0.6, -ticks / 8, "SMOKE")
      if ticks % 40 == 0 then
        for _, player in ipairs(context.boss:get_nearby_players(3)) do
          player:apply_potion_effect("darkness", 40, 0)
        end
      end
    end)
  end
}
