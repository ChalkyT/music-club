<script>
    export let about;
</script>

<p>{about}</p>

<style>
    @media only screen and (max-width: 330px) {
        p {
            font-size: 0.8rem;
        }
    }

    @media only screen and (max-width: 262px) {
        p {
            font-size: 0.6rem;
        }
    }
</style>