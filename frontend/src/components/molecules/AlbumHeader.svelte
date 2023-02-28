<script>
    import AlbumTitle from "../atoms/AlbumTitle.svelte";
    import AlbumGenre from "../atoms/AlbumGenre.svelte";

    export let title;
    export let artist;
    export let genre;
</script>

<div class="album-header">
    <AlbumTitle {title} {artist}/>
    <AlbumGenre {genre} />
</div>

<style>

</style>