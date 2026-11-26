-- Mareo Arcano (custom): al golpear, una espiral de humo morado envuelve al
-- jugador, la pantalla se marea (náusea) y se oscurece un instante.
return {
  api_version = 1,
  on_player_damaged_by_boss = function(context)
    if context.player == nil or not context.cooldowns:local_ready("mareo_arcano") then
      return
    end
    context.cooldowns:set_local(160, "mareo_arcano")
    local player = context.player
    player:apply_potion_effect("nausea", 140, 0)
    player:apply_potion_effect("darkness", 30, 0)
    local ticks = 0
    local task
    task = context.scheduler:run_every(1, function()
      ticks = ticks + 1
      if ticks > 30 or not player:is_alive() then
        context.scheduler:cancel_task(task)
        return
      end
      local l = player:get_location()
      local a = ticks / 2.5
      context.world:spawn_particle_at_location(em.create_location(
        l.x + math.cos(a) * 0.8, l.y + (ticks / 15), l.z + math.sin(a) * 0.8, l.world
      ), { particle = "WITCH", amount = 2, x = 0, y = 0, z = 0, speed = 0 }, 2)
    end)
  end
}
