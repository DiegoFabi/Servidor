# Pack Elites (MythicMobs)

Sustituye la conversión de élites de EliteMobs usando solo MythicMobs.

## Estructura
- `RandomSpawns/elites.yml`: cada mob hostil vanilla natural se REEMPLAZA por su versión élite
  (Chance 1, Priority 1). Las RandomSpawns de otros packs tienen prioridad x100, así que
  ratas, creepers, endermans, etc. siguen saliendo igual y los élites cubren el resto.
- `Mobs/plantillas.yml`: plantillas comunes (`elite_base`, `elite_guerrero`, `elite_arquero`).
- `Mobs/elites.yml`: un élite por tipo vanilla. Solo define tipo, nombre, familia y drops.
- `Skills/nucleo.yml`: nivel (tope 250), rango, nombre, tamaño, equipo, brillo y fuego.
- `Skills/poderes_*.yml`: poderes agrupados por tipo y los selectores que los reparten.
- `Items/equipo.yml`: armas y armaduras encantadas por rango.

## Niveles y rangos
Nivel = distancia al spawn (config-mobs.yml > WorldScaling) + 0-4 aleatorio, tope 250.

| Rango | Nivel | Color | Poderes |
|---|---|---|---|
| 1 Común | 1-24 | verde | 1 ofensivo |
| 2 Raro | 25-74 | azul | + 1 defensivo |
| 3 Épico | 75-124 | morado | + 1 especial de familia |
| 4 Legendario | 125-189 | naranja | + 1 mayor de familia |
| 5 Mítico | 190-250 | rojo | todos + brillo + velocidad |

## Rendimiento
- Sin temporizadores por mob: los poderes solo se lanzan al atacar o al recibir daño
  (los mobs quietos no gastan nada) y cada grupo tiene enfriamiento.
- Nombre vanilla (solo se ve al mirarlo) con la vida actualizada al recibir daño;
  la barra de vida es la nativa de MythicMobs y solo aparece tras recibir daño.
- Partículas con cantidades bajas y distancia de visión de 32 bloques.
