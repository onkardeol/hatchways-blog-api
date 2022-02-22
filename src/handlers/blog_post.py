class BlogPostHandler:
    def __init__(self, hatchways_facade):
        self.hatchways_facade = hatchways_facade

    def handle_blogs(self, tags, sort_by, direction):

        blog_set = self.hatchways_facade.fetch_blogs(tags)

        blog_list = {
            "posts": sorted(
                blog_set.values(),
                key=lambda sort_key: sort_key[sort_by],
                reverse=False if direction == "asc" else True,
            )
        }

        return blog_list
