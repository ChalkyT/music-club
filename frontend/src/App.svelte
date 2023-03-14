<script>
	import { onMount } from "svelte";
	import Album from './components/organisms/Album.svelte';
	import 'normalize.css';
	import Comments from "./components/organisms/Comments.svelte";

	export let name;


</script>

<main>
	<Album />
	<Comments />
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