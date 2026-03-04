# Customizing Claude Code Spinner Words

You can replace or extend Claude Code's spinner words with your own using the `spinnerVerbs` setting in `settings.json`.

> [Korean (한국어)](CUSTOMIZE_KR.md)

## What It Looks Like

When Claude Code is working, the spinner shows a random word from the list:

```
✢ ⛈️ Thundering 천둥치는중…
✢ 🤖 Clauding 클로딩하는중…
✢ 🍳 Cooking 요리하는중…
```

## How to Set Up

Edit `~/.claude/settings.json` and add the `spinnerVerbs` field:

```json
{
  "spinnerVerbs": {
    "mode": "replace",
    "verbs": [
      "⛈️ Thundering 천둥치는중",
      "🤖 Clauding 클로딩하는중",
      "🍳 Cooking 요리하는중"
    ]
  }
}
```

## Mode

| Mode | Description |
|------|-------------|
| `replace` | Replaces all default spinner words with your list |
| `append` | Keeps the defaults and adds your words on top |

## Verb Format

Each entry in `verbs` is a single string. Claude Code displays it as-is after the spinner symbol (`✢`).

```
"emoji EnglishWord 한국어"
```

You can use any combination:

- `"⛈️ Thundering 천둥치는중"` — emoji + English + Korean
- `"Thundering"` — English only
- `"⛈️ Thundering"` — emoji + English
- `"천둥치는중"` — Korean only

## Examples

### Full replacement with emoji + English + Korean

```json
{
  "spinnerVerbs": {
    "mode": "replace",
    "verbs": [
      "🧠 Thinking 생각하는중",
      "✍️ Writing 쓰는중",
      "🔍 Searching 검색하는중",
      "📚 Reading 읽는중",
      "⚙️ Processing 처리하는중"
    ]
  }
}
```

### English only (minimal)

```json
{
  "spinnerVerbs": {
    "mode": "replace",
    "verbs": [
      "Thinking",
      "Writing",
      "Searching",
      "Reading",
      "Processing"
    ]
  }
}
```

### Add a few custom words (keep defaults)

```json
{
  "spinnerVerbs": {
    "mode": "append",
    "verbs": [
      "🦄 Unicorning 유니콘타는중",
      "🍕 Pizza-making 피자굽는중"
    ]
  }
}
```

## Using This Project's Word Lists

This repository contains all 192 spinner words extracted from Claude Code, with Korean translations.

- **English**: [`words/2.1.63.md`](words/2.1.63.md)
- **Korean translations**: [`words/2.1.63_kr.md`](words/2.1.63_kr.md)

To use the full list with emoji + English + Korean, copy the `verbs` array from the example below. This is the same configuration used by the maintainer of this project:

<details>
<summary>Full 192-word settings.json example (click to expand)</summary>

```json
{
  "spinnerVerbs": {
    "mode": "replace",
    "verbs": [
      "✅ Accomplishing 완수하는중",
      "⚡ Actioning 실행하는중",
      "🌟 Actualizing 실현하는중",
      "🏗️ Architecting 설계하는중",
      "🍞 Baking 굽는중",
      "✨ Beaming 빛나는중",
      "🎷 Beboppin' 비밥추는중",
      "😵‍💫 Befuddling 헷갈리게하는중",
      "🌊 Billowing 부풀어오르는중",
      "🫕 Blanching 데치는중",
      "💨 Bloviating 장광설늘어놓는중",
      "🕺 Boogieing 부기추는중",
      "🤪 Boondoggling 삽질하는중",
      "👉 Booping 코찍는중",
      "🥾 Bootstrapping 부트스트래핑하는중",
      "🍺 Brewing 양조하는중",
      "🍔 Bunning 번만드는중",
      "🐿️ Burrowing 땅파는중",
      "🧮 Calculating 계산하는중",
      "💕 Canoodling 알콩달콩하는중",
      "🍮 Caramelizing 캐러멜화하는중",
      "💧 Cascading 쏟아지는중",
      "🚀 Catapulting 투석기발사하는중",
      "🧠 Cerebrating 골똘히생각하는중",
      "📡 Channeling 채널링하는중",
      "💃 Choreographing 안무짜는중",
      "🧈 Churning 휘젓는중",
      "🤖 Clauding 클로딩하는중",
      "🫧 Coalescing 합쳐지는중",
      "🤔 Cogitating 심사숙고하는중",
      "🔧 Combobulating 정리하는중",
      "🎼 Composing 작곡하는중",
      "💻 Computing 연산하는중",
      "🧪 Concocting 조합하는중",
      "🤨 Considering 고려하는중",
      "🧐 Contemplating 숙고하는중",
      "🍳 Cooking 요리하는중",
      "🛠️ Crafting 공들여만드는중",
      "🎨 Creating 창조하는중",
      "📊 Crunching 으드득씹는중",
      "💎 Crystallizing 결정화하는중",
      "🌱 Cultivating 재배하는중",
      "🔓 Deciphering 해독하는중",
      "⚖️ Deliberating 심의하는중",
      "🎯 Determining 결정하는중",
      "🫠 Dilly-dallying 꾸물거리는중",
      "😵 Discombobulating 혼란스럽게하는중",
      "✊ Doing 하는중",
      "✏️ Doodling 낙서하는중",
      "🌧️ Drizzling 이슬비뿌리는중",
      "🌙 Ebbing 빠져나가는중",
      "⚙️ Effecting 실행하는중",
      "💡 Elucidating 명쾌하게설명하는중",
      "🎀 Embellishing 꾸미는중",
      "🪄 Enchanting 마법거는중",
      "🔮 Envisioning 구상하는중",
      "♨️ Evaporating 증발하는중",
      "🫗 Fermenting 발효하는중",
      "🎻 Fiddle-faddling 빈둥거리는중",
      "🤹 Finagling 꼼수부리는중",
      "🔥 Flambéing 플람베하는중",
      "🗣️ Flibbertigibbeting 수다떠는중",
      "🌊 Flowing 흘러가는중",
      "😳 Flummoxing 어리둥절하게하는중",
      "🦋 Fluttering 펄럭이는중",
      "⚒️ Forging 벼려만드는중",
      "🫶 Forming 형성하는중",
      "🐸 Frolicking 뛰놀는중",
      "🧁 Frosting 프로스팅바르는중",
      "🏇 Gallivanting 쏘다니는중",
      "🐎 Galloping 질주하는중",
      "🌿 Garnishing 가니쉬올리는중",
      "⚡ Generating 생성하는중",
      "🌱 Germinating 싹틔우는중",
      "🙌 Gesticulating 몸짓하는중",
      "🐙 Gitifying Git화하는중",
      "🎶 Grooving 그루브타는중",
      "💨 Gusting 돌풍부는중",
      "🎵 Harmonizing 화음맞추는중",
      "🔐 Hashing 해싱하는중",
      "🐣 Hatching 부화하는중",
      "🐑 Herding 몰아가는중",
      "📯 Honking 빵빵울리는중",
      "🎪 Hullaballooing 야단법석피우는중",
      "🚀 Hyperspacing 초공간이동하는중",
      "💭 Ideating 아이디어내는중",
      "🌈 Imagining 상상하는중",
      "🎭 Improvising 즉흥연주하는중",
      "🥚 Incubating 품어키우는중",
      "🔍 Inferring 추론하는중",
      "🍵 Infusing 우려내는중",
      "⚛️ Ionizing 이온화하는중",
      "💃 Jitterbugging 지르박추는중",
      "🔪 Julienning 채써는중",
      "🫳 Kneading 반죽하는중",
      "🍞 Leavening 발효시키는중",
      "🧘 Levitating 공중부양하는중",
      "😴 Lollygagging 빈둥빈둥거리는중",
      "✨ Manifesting 현현하는중",
      "🫙 Marinating 재워두는중",
      "🐌 Meandering 구불구불흘러가는중",
      "🦎 Metamorphosing 변태하는중",
      "🌫️ Misting 안개뿜는중",
      "🌙 Moonwalking 문워크하는중",
      "🚶 Moseying 어슬렁거리는중",
      "🍷 Mulling 곰곰이생각하는중",
      "🎭 Musing 사색하는중",
      "💪 Mustering 모아들이는중",
      "☁️ Nebulizing 분무하는중",
      "🪺 Nesting 둥지트는중",
      "📰 Newspapering 신문만드는중",
      "🍜 Noodling 끄적거리는중",
      "⚛️ Nucleating 핵생성하는중",
      "🪐 Orbiting 궤도도는중",
      "🎻 Orchestrating 지휘하는중",
      "🧽 Osmosing 삼투하는중",
      "🚶‍♂️ Perambulating 거닐는중",
      "☕ Percolating 스며드는중",
      "📖 Perusing 정독하는중",
      "🏛️ Philosophising 철학하는중",
      "🌿 Photosynthesizing 광합성하는중",
      "🐝 Pollinating 수분하는중",
      "🤔 Pondering 곰곰이따지는중",
      "🎩 Pontificating 훈수두는중",
      "🐱 Pouncing 덮치는중",
      "🌧️ Precipitating 침전하는중",
      "🪄 Prestidigitating 마술부리는중",
      "⚙️ Processing 처리하는중",
      "📝 Proofing 교정하는중",
      "📡 Propagating 전파하는중",
      "🔨 Puttering 어물쩡거리는중",
      "🧩 Puzzling 퍼즐맞추는중",
      "⚛️ Quantumizing 양자화하는중",
      "💻 REPL'ing REPL돌리는중",
      "🌟 Razzle-dazzling 현란하게속이는중",
      "🎆 Razzmatazzing 왁자지껄하는중",
      "📚 Reading 읽는중",
      "🧠 Recalling 떠올리는중",
      "🔧 Recombobulating 다시정리하는중",
      "🔗 Reticulating 그물짜는중",
      "🐔 Roosting 횃대에앉는중",
      "🐄 Ruminating 되새김질하는중",
      "🍳 Sautéing 소테하는중",
      "🐿️ Scampering 종종걸음치는중",
      "🧳 Schlepping 끙끙대며나르는중",
      "🐁 Scurrying 종종거리는중",
      "🔎 Searching 검색하는중",
      "🧂 Seasoning 양념하는중",
      "🤡 Shenaniganing 장난치는중",
      "💫 Shimmying 시미추는중",
      "🫕 Simmering 뭉근히끓이는중",
      "🏃 Skedaddling 줄행랑치는중",
      "✏️ Sketching 스케치하는중",
      "🐍 Slithering 스르륵기어가는중",
      "🫠 Smooshing 뭉개는중",
      "🧦 Sock-hopping 삭스홉추는중",
      "🦇 Spelunking 동굴탐험하는중",
      "🌀 Spinning 빙글빙글도는중",
      "🌱 Sprouting 새싹돋는중",
      "🍲 Stewing 푹끓이는중",
      "🧊 Sublimating 승화하는중",
      "🌀 Swirling 소용돌이치는중",
      "🦅 Swooping 급강하하는중",
      "🧬 Symbioting 공생하는중",
      "🔬 Synthesizing 합성하는중",
      "🔥 Tempering 담금질하는중",
      "🧠 Thinking 생각하는중",
      "⛈️ Thundering 천둥치는중",
      "🔧 Tinkering 만지작거리는중",
      "🤪 Tomfoolering 어릿광대짓하는중",
      "🙃 Topsy-turvying 뒤죽박죽만드는중",
      "✨ Transfiguring 변모시키는중",
      "🪙 Transmuting 변환하는중",
      "🌪️ Twisting 비트는중",
      "🌊 Undulating 출렁이는중",
      "🌺 Unfurling 펼치는중",
      "🧶 Unravelling 풀어헤치는중",
      "😎 Vibing 바이브타는중",
      "🐧 Waddling 뒤뚱거리는중",
      "🚶 Wandering 방랑하는중",
      "🌌 Warping 워프하는중",
      "❓ Whatchamacalliting 거시기하는중",
      "🌀 Whirlpooling 소용돌이치는중",
      "⚡ Whirring 윙윙거리는중",
      "🥄 Whisking 휘휘젓는중",
      "〰️ Wibbling 흔들흔들하는중",
      "💼 Working 작업하는중",
      "🤠 Wrangling 씨름하는중",
      "✍️ Writing 쓰는중",
      "🍋 Zesting 제스트까는중",
      "⚡ Zigzagging 지그재그로가는중"
    ]
  }
}
```

</details>
