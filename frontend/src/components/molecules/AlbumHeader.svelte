<script>
    import AlbumTitle from "../atoms/AlbumTitle.svelte";
    import AlbumGenre from "../atoms/AlbumGenre.svelte";

    export let title = 'Album';
    export let artist = 'Artist';
    export let genre = 'Genre';
</script>

<div class="album-header">
    <AlbumTitle {title} {artist}/>
    <AlbumGenre {genre} />
</div>

<style>

</style>