<script>
    import AlbumHeader from "../molecules/Album/AlbumHeader.svelte";
    import AlbumInfo from "../molecules/Album/AlbumInfo.svelte";
    import {onMount} from "svelte";

	async function getAlbum() {
		let response = await fetch('api/albums/1');
        let data = await response.json();
        console.log(data.albums);
        return data.albums;
	}
</script>

{#await getAlbum()}
	<p>...waiting</p>
{:then data}
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
{:catch error}
	<p>An error occurred!</p>
{/await}


<style>

    .album-container {
        text-align: center;
        width: 75%;
        padding: 1rem;
        display: flex;
        flex-direction: column;
    }
</style>