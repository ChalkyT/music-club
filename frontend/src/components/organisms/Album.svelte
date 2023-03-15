<script>
    import AlbumHeader from "../molecules/Album/AlbumHeader.svelte";
    import AlbumInfo from "../molecules/Album/AlbumInfo.svelte";

    export let data;
</script>

<div class="album-container">
    <header>
        <AlbumHeader
                title={data.title}
                artist={data.artist}
                genre={data.genre}
        />
    </header>

    <main>
        <AlbumInfo
                title={data.title}
                artist={data.artist}
                imageUrl={data.artwork}
                about={data.about}
        />
    </main>

    <footer>

    </footer>
</div>

<style>

    .album-container {
        text-align: center;
        width: 75%;
        padding: 1rem;
        display: flex;
        flex-direction: column;
    }
</style>