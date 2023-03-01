<script>
    import CommentInput from "../atoms/CommentInput.svelte";
    import CommentSubmit from "../atoms/CommentSubmit.svelte";

    const handleSubmit = (e) => {
        e.preventDefault();
    }
</script>

<form on:submit={handleSubmit}>
    <CommentInput />
    <CommentSubmit />
</form>

<style>
    form {
        display: flex;
        flex-direction: column;
        width: 100%;
        margin-bottom: 1rem;
    }
</style>
