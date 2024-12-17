<span style="color:gray; font-size:0.7em">
Last change: {{ git.date.strftime("%b %d, %Y %H:%M:%S") }} {% if gitbranch != gitdefaultbranch %}
by {{ git.author }}
[branch: {{ gitbranch }} ({{ git.short_commit }})]
{% endif %}
</span>
