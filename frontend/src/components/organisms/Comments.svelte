<script>
    import CommentDisplay from "../molecules/CommentDisplay.svelte";
    import CommentForm from "../molecules/CommentForm.svelte";

    // Hardcoded data for now. TODO: Implement loading data from json/API with defaults for missing data.
    let comments = Array(5).fill({
        "user": 'A. User',
        "comment": 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut finibus metus orci, at dignissim arcu euismod ullamcorper. Curabitur venenatis pulvinar vulputate. Maecenas pellentesque ligula ut rutrum placerat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Maecenas sit amet lobortis nisl. Mauris aliquet, risus vel malesuada pharetra, nulla magna pulvinar nisi, et posuere felis nisi et turpis. Suspendisse eu finibus massa. Fusce a sem ex. Aliquam nullam.'
    });

    // Uncomment me and comment line 6-9 to test CommentDisplay and CommentForm with no existing comments
    // let comments = [];

    // When user submits a comment, add it to comments state and thank the user.
    // TODO: Create POST request to API (or JSON file for now) with new comment.
    const handleCommentSubmit = (e) => {
        // Add some dummy data for user.
        comments = [{"user": 'A. New. User', "comment": e.detail.comment}, ...comments];
        alert('Thanks for your comment!');
    }
</script>

<div class="comments-container">
<!--    Reinstantiate CommentForm when comments state changes to show the new comment-->
    {#key comments}
        <CommentForm on:commentsubmit={handleCommentSubmit}/>
    {/key}
    <CommentDisplay bind:comments={comments} />
</div>

<style>
    .comments-container {
        width: 75%;
        display: flex;
        flex-direction: column;
    }
</style>