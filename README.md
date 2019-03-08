# complimentr

[![BuyMeCoffee][buymecoffeebedge]][buymecoffee]
[![custom_updater][customupdaterbadge]][customupdater]

_Component to integrate with [complimentr][complimentr]._

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show a random compliment form the complimentr API.

![example][exampleimg]

## Installation

1. Using you tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `complimentr`.
4. Download _all_ the files from the `custom_components/complimentr/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Add `complimentr:` to your HA configuration.

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/complimentr/__init__.py
custom_components/complimentr/const.py
custom_components/complimentr/sensor.py
```

## Example configuration.yaml

```yaml
complimentr:
```


***

[exampleimg]: example.png
[buymecoffee]: https://www.buymeacoffee.com/ludeeus
[buymecoffeebedge]: https://camo.githubusercontent.com/cd005dca0ef55d7725912ec03a936d3a7c8de5b5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275792532306d6525323061253230636f666665652d646f6e6174652d79656c6c6f772e737667
[complimentr]: https://complimentr.com/api
[customupdater]: https://github.com/custom-components/custom_updater
[customupdaterbadge]: https://img.shields.io/badge/custom__updater-true-success.svg