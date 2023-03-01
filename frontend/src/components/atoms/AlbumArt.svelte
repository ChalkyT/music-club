<script>
    export let imageUrl;
    export let title;
    export let artist;
</script>

<img src="{imageUrl}" alt="Album art for {title} by {artist}" />

<style>
    img {
        width: 20rem;
    }

    @media only screen and (max-width: 450px) {
        img {
            width: 10rem;
        }
    }

    @media only screen and (max-width: 220px) {
        img {
            width: 5rem;
        }
    }
</style>