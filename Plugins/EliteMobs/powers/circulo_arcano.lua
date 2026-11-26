-- Círculo Arcano (custom): dibuja un círculo mágico bajo un jugador durante 2 s.
-- Si sigue dentro al cerrarse: daño, levitación corta y estallido de partículas.
local function circle(context, c, radius, particle, n)
  for i = 0, n - 1 do
    local a = i * (2 * math.pi / n)
    context.world:spawn_particle_at_location(em.create_location(
      c.x + math.cos(a) * radius, c.y + 0.1, c.z + math.sin(a) * radius, c.world
    ), { particle = particle, amount = 1, x = 0, y = 0, z = 0, speed = 0 }, 1)
  end
end

return {
  api_version = 1,
  on_boss_damaged_by_player = function(context)
    if not context.cooldowns:local_ready("circulo_arcano") or not context.cooldowns:global_ready() or math.random() > 0.35 then
      return
    end
    local players = context.boss:get_nearby_players(14)
    local target = players[math.random(1, math.max(1, #players))]
    if target == nil then
      return
    end
    context.cooldowns:set_local(300, "circulo_arcano")
    context.cooldowns:set_global(40)
    local l = target:get_location()
    local c = em.create_location(l.x, l.y, l.z, l.world)
    local ticks = 0
    local task
    task = context.scheduler:run_every(2, function()
      ticks = ticks + 2
      circle(context, c, 3, "ENCHANT", 24)
      circle(context, c, 2, "WITCH", 16)
      circle(context, c, 1, "ENCHANT", 8)
      if ticks >= 40 then
        context.scheduler:cancel_task(task)
        context.world:spawn_particle_at_location(em.create_location(c.x, c.y + 0.5, c.z, c.world),
          { particle = "EXPLOSION", amount = 3, x = 1.5, y = 0.3, z = 1.5, speed = 0 }, 3)
        for _, p in ipairs(context.boss:get_nearby_players(20)) do
          local pl = p:get_location()
          local dx, dz = pl.x - c.x, pl.z - c.z
          if dx * dx + dz * dz <= 9 and math.abs(pl.y - c.y) < 2.5 then
            p:apply_potion_effect("levitation", 25, 1)
          end
        end
        local entities = context.entities.get_nearby_entities(20, "living")
        for index = 1, #entities do
          local e = entities[index]
          if e.is_player then
            local el = e:get_location()
            local dx, dz = el.x - c.x, el.z - c.z
            if dx * dx + dz * dz <= 9 and math.abs(el.y - c.y) < 2.5 then
              e:deal_custom_damage(4)
            end
          end
        end
      end
    end)
  end
}
