<script>
    import AlbumArt from "../../atoms/Album/AlbumArt.svelte";
    import AlbumAbout from "../../atoms/Album/AlbumAbout.svelte";

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