<script>
    import CommentInput from "../atoms/CommentInput.svelte";
    import CommentSubmit from "../atoms/CommentSubmit.svelte";
    import {createEventDispatcher} from "svelte";

    const dispatch = createEventDispatcher();

    let textInput;

    // If there's any user input in textInput, send an event containing the input to Comments. Otherwise, nag the user.
    const handleSubmit = (e) => {
        e.preventDefault();
        if (textInput) {
            dispatch('commentsubmit', {
               comment: textInput
            });
        }
        else {
            alert('Please enter a comment!');
        }
    }

    // If the text box value from CommentInput changes, update textInput state.
    const handleTextBoxChange = (e) => {
        textInput = e.detail.text;
    }
</script>

<form on:submit={handleSubmit}>
    <CommentInput on:textboxchange={handleTextBoxChange} />
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
