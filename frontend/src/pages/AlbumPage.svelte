<script>
	import Album from '../components/organisms/Album.svelte';
	import Comments from "../components/organisms/Comments.svelte";

	export let currentRoute;

	async function getAlbum(id) {
        try {
            let response = await fetch(`/api/albums/${id}?format=json`);
            let data = await response.json();
            return data.albums;
        } catch (e) {
            throw new Error('Album not found')
        }
	}

</script>

<main>
	{#await getAlbum(currentRoute.namedParams.id)}
		<p>...waiting</p>
	{:then data}
		<Album {data}/>
		<Comments />
	{:catch error}
		<p>Album not found!</p>
	{/await}
</main>

<style>
	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin: 0 auto;
		font-family: "Bitstream Vera Sans Mono", Monaco, "Courier New", Courier, monospace;
	}
</style>