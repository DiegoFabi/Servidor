import yaml, glob, os, json
# Ejecutar desde /home/user/Servidor/Plugins
EM = 'EliteMobs/custombosses/event_megapack_2/'
EV = 'EliteMobs/customevents/event_megapack_2/'
OUT = 'MythicMobs/packs/Elites/'
NOMBRES = {'ancient_corpse':'Cadáver Ancestral','animated_armor':'Armadura Animada','annoyed_drowned':'Ahogado Furioso','banshee':'Banshee','banshee_summon':'Pena','beach_bug':'Bicho de Playa','beast_tamer':'Domador de Bestias','beast_tamer_summon':'Gran Bestia','beast_tamer_summon_1':'Bestia','big_bad_wolf':'Lobo Feroz','bloated_jeffrey':'Jeffrey el Hinchado','bloated_jeffrey_summon':'Amigo de Jeffrey','bone_fiend':'Demonio de Hueso','bone_fiend_mount':'Portador de Huesos','bone_skeleton':'Esqueleto de Hueso','circus_ringmaster':'Maestro de Ceremonias','circus_ringmaster_summon':'Animal Torturado','circus_ringmaster_summon_1':'Payaso Maltratado','circus_ringmaster_summon_2':'Globo Maldito','cursed_bandit':'Bandido Maldito','cursed_bandit_mount':'Araña Domesticada','divine_cinder':'Ceniza Divina','earth_mite':'Ácaro de Tierra','ender_guardian':'Guardián del End','ender_lapin':'Conejo del End','enders_1':'Enderchico','enders_2':'Endertipo','enders_3':'Enderamigo','endless_pursuer':'Perseguidor Eterno','enraged_snowman':'Muñeco de Nieve Furioso','exhumed_dead':'Muerto Exhumado','fire_conjurer':'Conjurador de Fuego','fire_conjurer_summon':'Llama Invocada','firestarter':'Incendiario','firestarter_mount':'Chispa','giant_magi':'Gigante Mago','jungle_lion':'León de la Selva','magma_construct':'Constructo de Magma','moonlight_devourer':'Devorador Lunar','moonlight_devourer_p2':'Devorador Lunar Despierto','morgana':'Morgana','morgana_mount':'Escoba de Bruja','mutated_mermaid':'Sirena Mutada','mutated_mermaid_summon':'Sirenito','nether_bovine':'Bovino Infernal','nether_hag':'Bruja del Nether','nether_wasp':'Avispa Infernal','nether_wasp_summon_1':'Invocadora de Colmena','nether_wasp_summon_2':'Avispa de Colmena','night_horder':'Acaparador Nocturno','rotting_diver':'Buzo Podrido','sand_fiend':'Demonio de Arena','sand_fiend_1':'Demonio de Arena','sand_fiend_2':'Demonio de Arena','skeleton_knight':'Caballero Esqueleto','sky_archer':'Arquero del Cielo','sky_archer_mount':'Corcel Celeste','smallstack':'Pilacorta (Cima)','smallstack_1':'Pilacorta (Medio)','smallstack_2':'Pilacorta (Medio)','smallstack_3':'Pilacorta (Medio)','smallstack_4':'Pilacorta (Base)','smallstack_5':'Pilacorta (Base)','smallstack_6':'Pilacorta (Portador)','sorcerer_supreme':'Hechicero Supremo','sorcerer_supreme_summon':'Siervo Eterno','starving_hog':'Cerdo Hambriento','storm_caller':'Invocador de Tormentas','storm_caller_p2':'Invocador de Tormentas Desatado','storm_caller_summon':'Siervo de la Tormenta','suspicious_phantom':'Phantom Sospechoso','suspicious_phantom_summon':'Llamarada','suspicious_phantom_summon_1':'Bombardero','the_great_weaver':'La Gran Tejedora','the_great_weaver_summon':'Madre de la Prole','the_great_weaver_summon_1':'Prole','the_hunter':'El Cazador','the_hunter_mount':'Bestia Domada','tiny_giant':'Gigante Diminuto','tree_trampler':'Pisoteador','tree_trampler_p2':'Pisoteador Furioso','undead_farmer':'Granjero No Muerto','undead_farmer_summon':'Orgullo del Granjero','undead_farmer_summon_1':'Cerdo Fallido','unwanted_visitor':'Visitante Indeseado','unwanted_visitor_summon':'Clon de Hielo','wandering_giant':'Gigante Errante','warlock':'Brujo','warlock_mount':'Demonio'}
for i in range(1, 11):
    NOMBRES[f'gremlin_{i}'] = 'Gremlin'
HP = {'ZOMBIFIED_PIGLIN':20,'HUSK':20,'DROWNED':20,'BLAZE':20,'WITHER_SKELETON':20,'ZOMBIE':20,'ZOGLIN':40,'GHAST':10,'SKELETON':20,'ENDERMAN':40,'RAVAGER':100,'BEE':10,'SPIDER':16,'STRAY':20,'PILLAGER':24,'PHANTOM':20,'WITCH':26,'POLAR_BEAR':30,'WOLF':20,'EVOKER':24,'SILVERFISH':8,'RABBIT':3,'CAVE_SPIDER':12,'ILLUSIONER':32,'VINDICATOR':24,'GUARDIAN':30}
DMG = {'ZOMBIFIED_PIGLIN':8,'HUSK':3,'DROWNED':3,'BLAZE':6,'WITHER_SKELETON':8,'ZOMBIE':3,'ZOGLIN':6,'GHAST':6,'SKELETON':3,'ENDERMAN':7,'RAVAGER':12,'BEE':2,'SPIDER':2,'STRAY':3,'PILLAGER':4,'PHANTOM':6,'WITCH':3,'POLAR_BEAR':6,'WOLF':4,'EVOKER':6,'SILVERFISH':1,'RABBIT':3,'CAVE_SPIDER':2,'ILLUSIONER':6,'VINDICATOR':13,'GUARDIAN':6}
ROT = {'attack_push':'po_empuje','attack_freeze':'po_hielo','attack_fire':'po_fuego','attack_arrow':'pf_flecha_arcana','arrow_rain':'pf_lluvia_flechas','attack_fireball':'pf_bola_fuego','ground_pound':'pf_golpe_suelo','plasma_blaster':'pf_plasma','lightning_bolts':'pf_tormenta_rayos','meteor_shower':'pj_lluvia_meteoros','bullet_hell':'pf_rafaga_flechas','attack_lightning':'po_rayo','thunderstorm':'pj_tormenta','firestorm':'pf_tormenta_fuego','attack_blinding':'po_ceguera','implosion':'pf_implosion','frost_cone':'pj_cono_helado','attack_weakness':'po_debilidad','tracking_fireball':'pf_bola_teledirigida','attack_gravity':'po_gravedad','attack_vacuum':'po_atraccion','attack_web':'pf_telarana','taze':'po_descarga','gold_explosion':'pj_explosion_dorada','attack_poison':'po_veneno','flamethrower':'pj_lanzallamas','flame_pyre':'pf_pira_llamas','gold_shotgun':'pj_escopeta_dorada','spirit_walk':'pf_salto_sombrio','arrow_fireworks':'pf_fuegos_artificiales','zombie_bloat':'pf_hinchazon','taunt':'pj_provocar','attack_confusing':'po_mareo','skeleton_tracking_arrow':'pj_flechas_guiadas'}
HIT = {'shield_wall':'pd_escudo','invisibility':'pd_invisibilidad','channel_healing':'pd_curacion','frost_walker':'pd_aura_helada'}
TRAIL = {'ELECTRIC_SPARK':'electric_spark','SMOKE_LARGE':'large_smoke','SMOKE_NORMAL':'smoke','FLAME':'flame','PORTAL':'portal','DRIP_LAVA':'dripping_lava','WHITE_ASH':'white_ash','BUBBLE_POP':'bubble_pop','WATER_BUBBLE':'bubble','SPELL_MOB':'witch','EXPLOSION_NORMAL':'poof','GOLD_NUGGET':'wax_off','BLOCK_DUST':'ash'}
EQ = {'mainHand':'HAND','offHand':'OFFHAND','helmet':'HEAD','chestplate':'CHEST','leggings':'LEGS','boots':'FEET'}

bosses = {os.path.basename(f)[:-4]: yaml.safe_load(open(f, encoding='utf-8')) for f in glob.glob(EM + '*.yml')}
mains, eventos = set(), []
for f in sorted(glob.glob(EV + '*.yml')):
    d = yaml.safe_load(open(f, encoding='utf-8'))
    if not d.get('isEnabled'):
        continue
    lst = [b[:-4] for b in d['bossFilenames']]
    mains.update(lst)
    eventos.append({'id': os.path.basename(f)[:-10], 'tipo': d['eventType'], 'spawn': (d.get('spawnType') or '').replace('.yml', ''),
                    'jefes': lst, 'chance': d.get('chance'), 'bloques': d.get('breakableMaterials') or []})
phases = {}
for k, b in bosses.items():
    for p in b.get('phases') or []:
        if ':' in p:
            fn, thr = p.split(':')
            phases[k] = (fn[:-4], float(thr))
p2 = {v[0] for v in phases.values()}
mid = lambda k: 'jefe_' + k
REF = {}
L = ["""# ============================================================
#  JEFES DE EVENTO (convertidos de EliteMobs event_megapack_2).
#  GENERADO por gen_jefes.py: nombres en español, vida/daño/velocidad,
#  equipo, tamaño, monturas, rastros, fases e invocaciones. Los poderes
#  de EliteMobs se traducen a los de Skills/ (rotación cada 3 s si tiene
#  objetivo). Cuándo y dónde salen: Skript/Elites/eventos.sk.
#  Principales (cuentan para el evento): plantilla elite_jefe_base.
#  Monturas, invocaciones y piezas: elite_jefe_esbirro.
# ============================================================"""]
for k in sorted(bosses):
    b = bosses[k]; t = b['entityType']; nom = NOMBRES.get(k, k)
    principal = k in mains or k in p2
    tpl = 'elite_jefe_base' if principal else 'elite_jefe_esbirro'
    hm = float(b.get('healthMultiplier', 1)); dm = float(b.get('damageMultiplier', 1))
    hp = round(HP.get(t, 20) * hm * (4 if principal else 1.5)); dmg = round(DMG.get(t, 3) * dm * (1.5 if principal else 1), 1)
    rot, hit, dmods, sk = [], [], [], []
    opts = {'MovementSpeed': b.get('movementSpeedAttribute', 0.25), 'FollowRange': b.get('followDistance', 40)}
    for p in b.get('powers') or []:
        if isinstance(p, dict):
            fn = p['filename'][:-4]; am = p.get('amount', 1); ch = p.get('chance', 1); st = p['summonType']
            if st == 'ONCE':
                sk.append(f"  - summon{{type={mid(fn)};amount={am};radius=4}} @self ~onSpawn {ch}")
            elif st == 'ON_COMBAT_ENTER':
                REF.setdefault(k, []).append((fn, am))
            else:
                sk.append(f"  - summon{{type={mid(fn)};amount={am};radius=3}} @self ~onDamaged {round(ch * 0.4, 2)}")
            continue
        n = p.replace('.yml', '')
        if n in ROT: rot.append(ROT[n])
        elif n in HIT: hit.append(HIT[n])
        elif n == 'invulnerability_fire': dmods += ['FIRE 0', 'FIRE_TICK 0', 'LAVA 0', 'HOT_FLOOR 0']
        elif n == 'invulnerability_arrow': dmods += ['PROJECTILE 0.1']
        elif n == 'invulnerability_fall_damage': dmods += ['FALL 0']
        elif n == 'invulnerability_knockback': opts['KnockbackResistance'] = 1
        elif n == 'movement_speed': opts['MovementSpeed'] = round(float(opts['MovementSpeed']) * 1.3, 3)
        elif n == 'corpse': sk.append("  - effect:particles{p=soul;a=30;hs=0.6;vs=1;s=0.05;y=1;vd=40} @self ~onDeath")
        elif n in ('bonus_coins', 'bonus_loot'): sk.append("  - addtag{tag=elite_evento_bonus} @self ~onSpawn")
    if k in REF:
        sk.append(f"  - skill{{s={mid(k)}_refuerzos}} @self ~onDamaged")
    if b.get('scale'): opts['Scale'] = b['scale']
    if b.get('isBaby'): opts['Scale'] = round(float(opts.get('Scale', 1)) * 0.6, 2)
    L.append(f"\n{mid(k)}:\n  Template: {tpl}\n  Type: {t}")
    L.append(f"  Display: '<#FF5C5C>☠ <#FFD36B>{nom} <#7E848F>Nv <caster.level>'")
    L.append(f"  Health: {hp}\n  Damage: {dmg}")
    if b.get('mountedEntity'):
        L.append(f"  Mount: {mid(b['mountedEntity'][:-4])}")
    L.append("  Options:")
    for a, v in opts.items(): L.append(f"    {a}: {v}")
    if dmods:
        L.append("  DamageModifiers:")
        for d in dict.fromkeys(dmods): L.append(f"  - {d}")
    eq = [f"  - {b[f].lower()} {s}" for f, s in EQ.items() if b.get(f)]
    if eq: L.append("  Equipment:"); L += eq
    L.append(f"  Variables:\n    nombre: {nom}")
    lines = []
    if rot: lines.append(f"  - randomskill{{s={','.join(dict.fromkeys(rot))}}} @target ~onTimer:60")
    if hit: lines.append(f"  - randomskill{{s={','.join(dict.fromkeys(hit))}}} @trigger ~onDamaged 0.35")
    for tr in b.get('trails') or []:
        if tr in TRAIL: lines.append(f"  - effect:particles{{p={TRAIL[tr]};a=2;hs=0.3;vs=0.4;s=0.01;y=0.5;vd=32}} @self ~onTimer:10")
    if k in phases: lines.append(f"  - skill{{s={mid(k)}_fase}} @self ~onDamaged")
    lines += sk
    if lines: L.append("  Skills:"); L += lines
S = ["# Fases y refuerzos de los jefes de evento (GENERADO por gen_jefes.py)"]
for k, (fn, thr) in phases.items():
    S.append(f"""{mid(k)}_fase:
  Conditions:
  - healthpercent{{h=<{int(thr * 100)}%}} true
  Skills:
  - effect:particles{{p=explosion;a=3;hs=0.6;vs=0.6;y=1;vd=40}} @self
  - effect:particlering{{p=soul_fire_flame;r=2.5;points=24;a=1;y=0.2;vd=40}} @self
  - sound{{s=entity.wither.spawn;v=0.6;p=1.4}} @self
  - message{{m="<#FF5C5C>☠ <#FFD36B><caster.var.nombre> <white>cambia de forma…"}} @PIR{{r=40}}
  - summon{{type={mid(fn)};amount=1}} @selflocation
  - remove @self""")
for k, lst in REF.items():
    S.append(f"{mid(k)}_refuerzos:\n  Conditions:\n  - variableequals{{var=caster.refuerzos;value=1}} false\n  Skills:\n  - setvariable{{var=caster.refuerzos;value=1;type=INTEGER}} @self\n" +
             '\n'.join(f"  - summon{{type={mid(fn)};amount={am};radius=4}} @self" for fn, am in lst))
open(OUT + 'Mobs/jefes_eventos.yml', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
open(OUT + 'Skills/jefes_fases.yml', 'w', encoding='utf-8').write('\n\n'.join(S) + '\n')
json.dump({'eventos': eventos, 'nombres': NOMBRES}, open(os.path.join(os.path.dirname(__file__), 'eventos.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print(len(bosses), 'jefes', len(eventos), 'eventos', 'fases', phases)
