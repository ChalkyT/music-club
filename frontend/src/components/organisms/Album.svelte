<script>
    import AlbumHeader from "../molecules/AlbumHeader.svelte";
    import AlbumInfo from "../molecules/AlbumInfo.svelte";

    // Hardcoded data for now. TODO: Implement loading data from json with defaults for missing data.
    let album = {
        "art": 'https://upload.wikimedia.org/wikipedia/en/f/f8/10000Days.jpg',
        "title": '10000 Days',
        "artist": 'Tool',
        "genre": 'Progressive Metal/Rock',
        "about": 'Overrated? Not at all! It\'s not my fault you can\'t pay attention to songs over 3 minutes long.'
    }
</script>

<div class="album-container">
    <header>
        <AlbumHeader
                title={album.title}
                artist={album.artist}
                genre={album.genre}
        />
    </header>

    <main>
        <AlbumInfo
                title={album.title}
                artist={album.artist}
                imageUrl={album.art}
                about={album.about}
        />
    </main>

    <footer>

    </footer>
</div>


<style>
    .album-container {
        width: 100%;
        border: #FF0000 solid 1px;
    }
</style>