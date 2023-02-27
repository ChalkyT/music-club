<script>
    import AlbumTitle from "../atoms/AlbumTitle.svelte";

    export let title;
    export let artist;
    export let genre;
</script>

<div class="album-header">
    <AlbumTitle {title} {artist}/>
    <p>{genre}</p>
</div>

<style>

</style>