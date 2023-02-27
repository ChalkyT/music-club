<script>
	import { onMount } from "svelte";
	import Album from './components/album.svelte';

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
	<h3>Data from server API</h3>
	{apiMessage}
</main>

<style>
	main {
		text-align: center;
		margin: 0 auto;
	}
</style>