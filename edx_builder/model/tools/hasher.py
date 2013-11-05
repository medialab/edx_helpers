# -------------------------------------------------------------------
# EdxBuilder hasher
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
import md5
import random

# Hashing a feed to generate element identifier
def hashid(feed):
    m = md5.new()
    m.update(unicode(feed) + unicode(random.randint(1, 100)))
    return m.hexdigest()