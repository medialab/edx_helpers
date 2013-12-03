#EdxBuilder

##Concept
The aim of the EdxBuilder command line tool is to compile a folder (or zipped folder) containing an EDX course written in a Markdown subset syntax into a tar.gz file that can be imported into EDX Studio.

##Installation
To quicly install the tool on an unix-based system, clone this repository and install dependencies (preferably in a virtualenv)

```bash
git clone https://github.com/medialab/edx_helpers.git
cd edx_helpers/edx_builder
pip install -r requirements.txt
```

Then copy the **config/settings.default.yml** file and indicate your scribd api reference in it if you plan to use the feature.

```bash
cp config/settings.default.yml config/settings.yml
vi config/settings.yml
```

Edit the yaml file there

```yaml
# Generic Settings
settings:
    scribd:
        key: 'your-scribd-key'
        secret: 'your-scribd-secret'
```

You are now good to go.

##Usage
To compile a folder or a zip file, simply run the following command

```bash
python edx_builder.py build [path/to/folder-or-zipfile]
```

It will compile to an **output/** folder. If you want to specify the output directory use the following option

```bash
python edx_builder.py build [path/to/folder-or-zipfile] -o/--output {output/directory}
```

Whenever lost, you can use the help option

```bash
python edx_builder.py -h/--help
```

##Folder Structure
To be properly compiled, the processed folder must have those three requisites

1. A YAML configuration file for the course named **course_layout.yml** at the root of the folder.
2. A **static** folder (default name), holding every static file needed for your course (images, subtitles...).
3. One folder per section containing one folder per subsection finally containing one markdown file per unit.

##YAML Configuration File
This is an example of what the **course_layout.yml** file may be

```yaml
advanced_modules: []
course_image: 'cover.png'
name: 'EdxBuilder Test Course'
identifier: '2014_Fall'
organization: 'UniversityX'
number: 'TS101'
start: '2013-10-28T11:00:00Z'
static: 'static'
sections:
    - name: 'Section #1'
      start: '2013-10-28T12:00:00Z'
      directory: 'section1'
      subsections:
        - name: 'Subsection #1-1'
          start: '2013-10-28T12:00:00Z'
          directory: 'subsection1'
          units:
            - name: 'Unit 1-1-1'
              path: 'unit1'
            - name: 'Unit 1-1-2'
              path: 'unit2'
            - name: 'Unit 1-1-3'
              path: 'unit3'
            - name: 'Unit 1-1-4'
              path: 'unit4'
            - name: 'Unit 1-1-5'
              path: 'unit5'
        - name: 'Subsection #2-1'
          start: '2013-10-28T12:00:00Z'
          directory: 'subsection2'
          units:
            - name: 'Unit 1-1-1'
              path: 'unit1'
            - name: 'Unit 1-1-2'
              path: 'unit2'
            - name: 'Unit 1-1-3'
              path: 'unit3'
```
TODO: more documentation about this precise points.

##Writing a unit
A unit, in the edx_builder format, is expressed by a single markdown file that holds every needed component separated by a line of three stars (* * *).

Example of component

```markdown
component: html
name: Political Failure

#Title
**bold** text.

![image description](/static/image.png)

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed blandit eros. Proin in elit lectus. Donec at felis urna. Cras gravida nunc mi, vel ultricies lectus mollis vel. Mauris ut magna mattis, semper tellus ac, sollicitudin lacus. Nam erat ante, facilisis id consequat quis, imperdiet a tellus. Quisque mauris turpis, pharetra eget nisl eu, luctus eleifend nisi. In volutpat orci vitae enim imperdiet dignissim. Aliquam ut odio pretium, euismod lectus ac, condimentum nisl. Sed mollis urna ut elit pretium lobortis. Morbi eu ante ligula. Ut mi tortor, ullamcorper sed blandit semper, pulvinar sit amet tellus.
```

Example of whole unit

```markdown
component: html
name: Political Failure

#Title
**bold** text.

* * *

component: video
id: KL_v-y0AneEgit stat
name: Test Video

* * *

component: html
name: Political Failure

#Title
*italic* text.
```

###Components
Every component **must** start with a header indicating at least its type (html, video or discussion) and some metadatas. It must be written in yaml style (key: value - precisely, spaces are important).

###Html component
A html component **must** have a name metadata (this is the name displayed while hovering on the menu bar of edx in a subsection). After this name is given, write every needed piece of text in markdown.

Example

```markdown
component: html
name: Political Failure

#Title
**bold** text.

![image description](/static/image.png)
```

###Video component
A video component **must** have the following metadatas:

1. A name {name}
2. A Youtube id {youtube_id} (typically, on a youtube url like http://www.youtube.com/watch?v=98BIu9dpwHU, the id is this final part after ?v= --> "98BIu9dpwHU")

Example

```markdown
component: video
id: KL_v-y0AneEgit stat
name: Test Video
```

###Discussion component
A discussion component **must** have the following metadatas:

1. A name {name}
2. A category name {category_name} The name of the forum section holding the discussion.
3. A subcategory_name {subcategory_name} The name of the forum subsection holding the discussion.

Example

```markdown
component: discussion
category: Category_name
subcategory: Subcategory_name
name: Name in hover
```

##Markdown Syntax Subset
TODO

###Standard Markdown Elements
TODO

###Custom Markdown Elements
scribd
floating image
separating component

##Help & Examples
If you feel lost about folder structure and the custom mardown syntax we use here, visit the **tests/test_course** section of this repository to see an complete example.

##Dependencies

    colifrapy
    lxml
    Markdown
    pyyaml
    python-scribd