-- Salto Sombrío (custom): el élite desaparece entre partículas de portal y
-- reaparece a la espalda de su objetivo.
return {
  api_version = 1,
  on_boss_damaged_by_player = function(context)
    if not context.cooldowns:local_ready("salto_sombrio") or math.random() > 0.20 then
      return
    end
    local target = context.boss:get_target_player()
    if target == nil then
      return
    end
    local b = context.boss:get_location()
    local p = target:get_location()
    local dir = context.vectors.normalize_vector(context.vectors.get_vector_between_locations(b, p))
    local dest = em.create_location(p.x + dir.x * 2, p.y, p.z + dir.z * 2, p.world)
    if not context.world:is_passthrough_at_location(dest) then
      return
    end
    context.cooldowns:set_local(240, "salto_sombrio")
    context.world:spawn_particle_at_location(b, { particle = "PORTAL", amount = 60, x = 0.4, y = 1, z = 0.4, speed = 0.6 }, 60)
    context.world:play_sound_at_location(b, "ENTITY_ENDERMAN_TELEPORT", 1.0, 0.8)
    context.boss:teleport_to_location(dest)
    context.world:spawn_particle_at_location(dest, { particle = "REVERSE_PORTAL", amount = 60, x = 0.4, y = 1, z = 0.4, speed = 0.05 }, 60)
  end
}
