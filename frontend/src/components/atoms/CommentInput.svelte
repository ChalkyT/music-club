<script>
    import {createEventDispatcher} from "svelte";

    const dispatch = createEventDispatcher()

    let defaultText = 'Enter your comment here...';

    const handleFocus = (e) => {
        if (e.target.value === defaultText) {
            e.target.value = '';
        }
    }

    const handleFocusOut = (e) => {
        if (e.target.value === '') {
            e.target.value = defaultText;
        }
    }

    const handleChange = (e) => {
        if (e.target.value !== defaultText) {
            dispatch('textboxchange', {
                text: e.target.value
            });
        }
    }
</script>

<label for="comment_box">Your comment:</label>
<textarea on:change={handleChange} on:focus={handleFocus} on:focusout={handleFocusOut} id="comment_box" name="comment_box" rows="5">{defaultText}</textarea>

<style>
    label, textarea {
        font-size: 0.8rem;
        margin-bottom: 1rem;
    }
</style>