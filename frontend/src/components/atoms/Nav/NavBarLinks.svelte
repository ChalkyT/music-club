<script>
    let links = [
        {"title": 'Post', "link": "#"},
        {"title": 'Albums', "link": "#"},
        {"title": 'Archive', "link": "#"},
        {"title": 'Profile', "link": "#"}
    ];
</script>

<div class="link-container">
    {#each links as link}
        <a href="{link.url}">{link.title}</a>
    {/each}
</div>

<style>
    .link-container {
        grid-area: navlinks;
        display: flex;
        justify-content: space-around;
    }
</style>
