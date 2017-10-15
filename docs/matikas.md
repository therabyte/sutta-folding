# What are Matikas?

> [(Gethin, 1992)](@Gethin1992) A monk is "one who has heard much, one to whom the tradition has been handed down, learned in the Dharma [dhamma.dhana], learned in the vinaya [vinaya.dhana], learned in the matika [matika.dhana]."

> "It would appear, then, that a matika can be any schedule or table of terms or lists, but especially one built up according to a system of numerical progression, that acts as a basis for further exposition."

> [P. 161](@Gethin1992) "We can sum up by saying that matikas contain the building blocks for constructing an exposition or text. But they are magical building blocks; when combined and used in various ways they can create a palace that us much longer in extent than the sum of the parts.
If the lists and schedules that we have been considering are matikas, then someone who is matika.dhana or 'learned in the matikas' is presumably someone who knows these and similar lists. [...]. He also knows what to do with them; in other words, he knows how to expand them and draw out expositions from them. [...] not simply someone who can spout endless lists of lists learnt by heart, but a person who can improvise and create through the medium of these lists."

> [P.158](@Gethin1992) "The feeling that in the present context the sequence dhamma vinaya matika ought to correspond to the sequence sutta vinaya abhidhamma is backed up by certain accounts of the first Buddhist council surviving in Chinese and Tibetan translation, which relate that after Ananda had recited the Sutranta and Upali the Vinaya, Mahakasyapa recited the Matikas."


Lists constitutive of the Samyuttanikaya according to Gethin p.162 (core matikas):
- The five aggregates
- The six sense spheres
- The twelwe links of dpendeng arising
- The four application of mindfulness
- The four right endeavour
- The four bases of success
- The five faculties
- The five powers
- The seven factors of awakening
- The noble eightfold path

> [P. 164](@Gethin1992) "In considering the Dhammasangani and Vibhanga it is not unhelpful [...] to see the triplet-couplet matika and the core matika as acting like the two axes of the Abhidhamma method. [...] The Dhammasangani treats the core matikas by way of the triplet-couplet matika [and the Vibhanga does the inverse]. [...]


## Coding Matikas for the project

In this project, we chose to code matikas as [lists written in plain language in a markdown format](../data/matikas.md). Here's how we wrote them down.

```
## title in plan language

id: system id for reference

* expressions in english coding the matika, using english/pali codes
* expressions in english coding the matika, using english/pali codes
* expressions in english coding the matika, using english/pali codes
* expressions in english coding the matika, using english/pali codes
```

There may be free additions in there, but they are not parsed yet.

In this description, the words in pali are coded using the format:

```
[english word](@[p]paliword)
```

`[p]` here codes for a word in **Pali**. There may be some Sanskrit words later.

Example:
```
[suffering](@[p]dukkha)
[arising](@[p]samudaya)
[cessation](@[p]nirodha)
[path]([p]magga)
```

### Example (four noble truths)

```
## Four [noble](@[p]sacca) truths

id: four noble truths

_or four truths of the nobles_

noble: [sacca](@[p]sacca), [satya](@[s]satya)

* [suffering](@[p]dukkha)
* the [arising](@[p]samudaya) of [suffering](@[p]dukkha)
* the [cessation](@[p]nirodha) of [suffering](@[p]dukkha)
* the eightfold [path]([p]magga) that leads to the [cessation](@[p]nirodha) of [suffering](@[p]dukkha)

Ref:
- Dhammapada, 190-191
- Dhammacakkappavattana-sutta
- Rahula W., L'Enseignement du Bouddha, p. 35
- Eracle J., Paroles du Bouddha, p. 25
```


## Biblio

- [Gethin R.M.L., The Matikas: memorization, mindfulness and the list, 1992](@Gethin1992)
