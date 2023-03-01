<script>
    import CommentInput from "../atoms/CommentInput.svelte";
    import CommentSubmit from "../atoms/CommentSubmit.svelte";

    let textInput;

    const handleSubmit = (e) => {
        e.preventDefault();
        if (textInput) {
            alert('Thanks for your comment!');
            console.log(textInput);
        }
        else {
            alert('Please enter a comment!');
        }
    }

    const handleTextBoxChange = (e) => {
        textInput = e.detail.text;
    }
</script>

<form on:submit={handleSubmit}>
    <CommentInput on:textboxchange={handleTextBoxChange}/>
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
