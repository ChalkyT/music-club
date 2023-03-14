<script>
	import 'normalize.css';
    import {Router} from "svelte-router-spa";
    import {routes} from "./routes";

</script>

<Router {routes} />

<style>
	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin: 0 auto;
		font-family: "Bitstream Vera Sans Mono", Monaco, "Courier New", Courier, monospace;
	}
</style>