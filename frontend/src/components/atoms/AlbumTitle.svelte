<script>
    export let title;
    export let artist;
</script>

<h2>{title} - {artist}</h2>

<style>
    @media only screen and (max-width: 330px) {
        h2 {
            font-size: 1.2rem;
        }
    }

    @media only screen and (max-width: 262px) {
        h2 {
            font-size: 0.7rem;
        }
    }
</style>