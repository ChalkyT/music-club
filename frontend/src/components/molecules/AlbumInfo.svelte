<script>
    import AlbumArt from "../atoms/AlbumArt.svelte";
    import AlbumAbout from "../atoms/AlbumAbout.svelte";

    export let imageUrl;
    export let title;
    export let artist;
    export let about;
</script>

<div class="album-info">
    <AlbumArt {imageUrl} {title} {artist} />
    <AlbumAbout {about} />
</div>


<style>

</style>