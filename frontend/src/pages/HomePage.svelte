<script>
    import AlbumTitle from "../components/atoms/Album/AlbumTitle.svelte";
    import AlbumArt from "../components/atoms/Album/AlbumArt.svelte";

    export let params;
    export let currentRoute;

    async function getAlbums() {
            try {
                let response = await fetch('/api/albums/?format=json');
                let data = await response.json();
                return (data.albums);
            } catch (e) {
                throw new Error('No albums found')
            }
        }

</script>

<h1>Album Club</h1>
{#await getAlbums()}
		<p>...waiting</p>
{:then albums}
    {#each albums as album}
        <a href={`/album/${album.id}`}>
            <AlbumTitle title={album.title} artist={album.artist} />
            <AlbumArt imageUrl={album.artwork} artist={album.artist} title={album.title}/>
        </a>
    {/each}
{:catch error}
		<p>No albums found!</p>
{/await}