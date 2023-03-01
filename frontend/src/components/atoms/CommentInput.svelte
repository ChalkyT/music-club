<script>
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
</script>

<label for="comment_box">Your comment:</label>
<textarea on:focus={handleFocus} on:focusout={handleFocusOut} id="comment_box" name="comment_box" rows="5">{defaultText}</textarea>

<style>
    label, textarea {
        font-size: 0.8rem;
        margin-bottom: 1rem;
    }
</style>