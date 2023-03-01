<script>
	import { onMount } from "svelte";
	import Album from './components/organisms/Album.svelte';
	import 'normalize.css';
	import Comments from "./components/organisms/Comments.svelte";

	export let name;

	let apiMessage = 'Waiting for server...';

	onMount(async  () => {
		let response = await fetch('api/greet')
				.then((res) => res.json());
		console.log(response);
		apiMessage = JSON.stringify(response);
	});
</script>

<main>
	<Album />
	<Comments />
	<h3>Data from server API</h3>
	{apiMessage}
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