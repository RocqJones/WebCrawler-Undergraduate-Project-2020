pages = []
base_url = 'https://www.mfarm.co.ke/posts'
pages.append(base_url)
for i in range(2, 200):
    other_pages = 'https://www.mfarm.co.ke/posts?page=' + str(i)
    pages.append(other_pages)

print(pages)