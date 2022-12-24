import slugify



def main():

    text = " slug if y "
    f = slugify.slugify(text)
    print(f)

if __name__ == '__main__':
    main()
