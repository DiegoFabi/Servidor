# Scripts de Skript

Skript carga las subcarpetas automáticamente. Un archivo que empieza con `-` está desactivado.

| Carpeta | Contenido |
|---|---|
| `utils/` | Librerías **globales** reutilizables: `items.sk` (quitar/dar items, buzón), `notificaciones.sk` (sonido suave notificar()), autopickup, cosecha, `limpieza.sk` (objetos del suelo) y `perfil.sk` (Mi Perfil) |
| `magia/` | Poderes. `nucleo_magia.sk` (fxRing, fxLinea, protección de caída) y `menu_magia.sk` (/magia) |
| `magia/comunes/` | `curacion_espiral.sk` (/spiralheart), `misil_de_agua.sk` (/watermisil), `salto_explosivo.sk` (/blastpower), `nova_de_escarcha.sk` (/escarcha), `bendiciones.sk` (/bendicion <tipo>: mecánicas propias de pociones, anillos, gemas y reliquias), `pergaminos.sk` (/pergamino <tipo>: 6 pergaminos) |
| `magia/raros/` | `bola_de_fuego.sk` (/explosionmagic), `garras_de_dragon.sk` (/clawstrike), `campo_de_gravedad.sk` (/gravity), `cadena_de_rayos.sk` (/cadenarayos) |
| `magia/malditos/` | `objetos_malditos.sk` (/maldicion <tipo>: 5 poderes con precio para el portador) |
| `magia/avanzados/` | `clase_humano.sk` (/humano), `ira_del_cielo.sk` (/iradelcielo), `meteoro_arcano.sk` (/meteoro) |
| `economia/` | Sistemas con money de ExcellentEconomy: `coinflip.sk`, `subasta.sk` |
| `minijuegos/` | `chat_minigames.sk`, `ruleta.sk`, `busca_objetos.sk` (1v1 cada 80 min y evento de la ruleta roja), `veneno_toxico.sk` (evento de la ruleta roja), `reto_clicks.sk` (/retoclicks), `tres_en_raya.sk` (/tresenraya, 1v1 con apuesta cada 55 min) |
| `items/` | Comportamiento global de items: `tooltip_style.sk` (fondo de tooltip por custom_data), `durabilidad.sk` (usos limitados por custom_data `usos`, /desgastar) |
| `personalizacion/` | `particulas_cosmeticas.sk` (7 partículas decorativas que se compran con Shards en CoreTools) |
| `servidor/` | MOTD, `anuncios.sk` (único script de anuncios globales, p. ej. tótems) y `tutorial.sk` (puente del tutorial de TypeWriter + menú `/historia`) |
| `examples/` | Ejemplos de Skript (desactivados) |

## Librería global `utils/items.sk`

| Uso | Desde |
|---|---|
| `itemQuitar(p, tipo, n)`, `itemContar(p, tipo)`, `itemDar(jugador, item)`, `buzonReclamar(p)` | Otros scripts |
| `itemquitar <jugador> <cantidad> <item> [comando si se cobró]` | Consola, MythicMobs, CoreTools |
| `itemdar <jugador> <cantidad> <item>` (si no cabe, va al buzón) | Consola, MythicMobs, CoreTools |
| `/buzon` | Jugadores |

## Reglas

- Nada específico: si algo se puede reutilizar, va como función o comando global en `utils/`.
- Sin temporizadores periódicos: solo eventos y `wait` puntuales.
- Inventarios, economía y entidades solo se tocan en el hilo principal (API de Bukkit);
  el resto se mantiene ligero: variables en memoria `{-...}` y sin bucles sobre el mundo.
- Mensajes con MiniMessage y sin colores `#` dentro de `options:`.
