# {{cookiecutter.project_name}}

An empty research project created from [https://github.com/adamaltmejd/research-project-template](Adam Altmejd's research template).

{%- if cookiecutter.license[:1] == '1' -%}
## License

Copyright (c) {% now 'local', '%Y' %} {{ cookiecutter.full_name }}

All code and research materials are distributed under the [MIT license](https://opensource.org/licenses/MIT).

{%- elif cookiecutter.license[:2] == '2' -%}
## License

Copyright (c) {% now 'local', '%Y' %} {{ cookiecutter.full_name }}

All source code is distributed under the [MIT license](https://opensource.org/licenses/MIT). The published data, and research materials are available under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

SPDX-License-Identifier: MIT AND CC-BY-SA-4.0
{%- elif cookiecutter.license[:3] == '3' -%}
{%- endif %}
