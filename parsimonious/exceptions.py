class UndefinedLabel(Exception):
    """A rule referenced in a grammar was never defined.

    Circular references and forward references are okay, but you have to define
    stuff at some point.

    """
    def __init__(self, label):
        self.label = label

    def __unicode__(self):
        return u'The label "%s" was never defined.' % self.label

    __str__ = __unicode__


class VisitationException(Exception):
    """Something went wrong while traversing a parse tree.

    This exception exists to augment an underlying exception with information
    about where in the parse tree the error occurred. Otherwise, it could be
    tiresome to figure out what went wrong; you'd have to play back the whole
    tree traversal in your head.

    """
    def __init__(self, exc, exc_class, node):
        """Construct.

        :arg exc: What went wrong. We wrap this and add more info.
        :arg node: The node at which the error occurred

        """
        super(VisitationException, self).__init__(
            '%s: %s\n\n'
            'Parse tree:\n'
            '%s' %
            (exc_class.__name__,
             exc,
             node.prettily(error=node)))
