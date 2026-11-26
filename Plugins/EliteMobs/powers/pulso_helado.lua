-- Pulso Helado (custom): una onda de copos se expande desde el élite; los
-- jugadores que alcanza quedan ralentizados y con fatiga.
return {
  api_version = 1,
  on_boss_damaged_by_player = function(context)
    if not context.cooldowns:local_ready("pulso_helado") or not context.cooldowns:global_ready() or math.random() > 0.30 then
      return
    end
    context.cooldowns:set_local(300, "pulso_helado")
    context.cooldowns:set_global(40)
    local l = context.boss:get_location()
    local c = em.create_location(l.x, l.y, l.z, l.world)
    local radius = 0
    local hit = {}
    local task
    task = context.scheduler:run_every(1, function()
      radius = radius + 0.5
      local n = math.floor(radius * 8)
      for i = 0, n - 1 do
        local a = i * (2 * math.pi / n)
        context.world:spawn_particle_at_location(em.create_location(
          c.x + math.cos(a) * radius, c.y + 0.3, c.z + math.sin(a) * radius, c.world
        ), { particle = "SNOWFLAKE", amount = 1, x = 0, y = 0, z = 0, speed = 0 }, 1)
      end
      for _, p in ipairs(context.boss:get_nearby_players(7)) do
        local pl = p:get_location()
        local d = math.sqrt((pl.x - c.x) ^ 2 + (pl.z - c.z) ^ 2)
        local key = tostring(p)
        if math.abs(d - radius) < 0.7 and not hit[key] then
          hit[key] = true
          p:apply_potion_effect("slowness", 80, 2)
          p:apply_potion_effect("mining_fatigue", 80, 1)
        end
      end
      if radius >= 6 then
        context.scheduler:cancel_task(task)
      end
    end)
  end
}
