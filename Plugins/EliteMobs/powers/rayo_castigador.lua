-- Rayo Castigador (custom): marca el suelo del jugador con chispas durante
-- 1,5 s y luego cae un rayo real en ese punto (se puede esquivar).
return {
  api_version = 1,
  on_boss_damaged_by_player = function(context)
    if not context.cooldowns:local_ready("rayo_castigador") or not context.cooldowns:global_ready() or math.random() > 0.30 then
      return
    end
    local target = context.boss:get_target_player()
    if target == nil then
      local players = context.boss:get_nearby_players(16)
      target = players[1]
    end
    if target == nil then
      return
    end
    context.cooldowns:set_local(200, "rayo_castigador")
    context.cooldowns:set_global(40)
    local l = target:get_location()
    local mark = em.create_location(l.x, l.y, l.z, l.world)
    local ticks = 0
    local task
    task = context.scheduler:run_every(2, function()
      ticks = ticks + 2
      for i = 0, 15 do
        local a = (i * math.pi / 8) + ticks / 6
        context.world:spawn_particle_at_location(em.create_location(
          mark.x + math.cos(a) * 1.5, mark.y + 0.1, mark.z + math.sin(a) * 1.5, mark.world
        ), { particle = "ELECTRIC_SPARK", amount = 1, x = 0, y = 0, z = 0, speed = 0 }, 1)
      end
      if ticks >= 30 then
        context.scheduler:cancel_task(task)
        context.world:strike_lightning_at_location(mark)
      end
    end)
  end
}
