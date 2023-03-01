<script>
    export let genre;
</script>

<p>{genre}</p>

<style>
    @media only screen and (max-width: 330px) {
        p {
            font-size: 0.8rem;
        }
    }

    @media only screen and (max-width: 262px) {
        p {
            font-size: 0.5rem;
        }
    }
</style>