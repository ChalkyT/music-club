<script>
    import PageTitle from "../atoms/Page/PageTitle.svelte";
    import NavBar from "../molecules/Nav/NavBar.svelte";

    let title = 'Music Club';
</script>

<div class="header">
    <PageTitle {title} />
    <NavBar />
</div>

<style>
    .header {
        width: 100%;
        display: grid;
        background-color: #f7e1b5;
        padding-bottom: 1rem;
        grid:
            'title'
            'navbar';
        align-items: center;
    }
</style>
