<script>
    import CommentDisplay from "../molecules/CommentDisplay.svelte";

    // Hardcoded data for now.
    let comments = Array(5).fill({
        "user": 'A. User',
        "comment": 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut finibus metus orci, at dignissim arcu euismod ullamcorper. Curabitur venenatis pulvinar vulputate. Maecenas pellentesque ligula ut rutrum placerat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Maecenas sit amet lobortis nisl. Mauris aliquet, risus vel malesuada pharetra, nulla magna pulvinar nisi, et posuere felis nisi et turpis. Suspendisse eu finibus massa. Fusce a sem ex. Aliquam nullam.'
        });
</script>

<div class="comments-container">
    <CommentDisplay {comments} />
</div>

<style>
    .comments-container {
        width: 75%;
        display: flex;
        flex-direction: column;
    }
</style>