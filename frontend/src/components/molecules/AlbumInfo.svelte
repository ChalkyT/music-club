<script>
    import AlbumArt from "../atoms/AlbumArt.svelte";
    import AlbumAbout from "../atoms/AlbumAbout.svelte";

    export let imageUrl = 'https://placekeanu.com/250/g';
    export let title = 'Album';
    export let artist = 'Artist';
    export let about = 'The server gnomes were unable to find a description of the album :(';
</script>

<div class="album-info">
    <AlbumArt {imageUrl} {title} {artist} />
    <AlbumAbout {about} />
</div>


<style>

</style>