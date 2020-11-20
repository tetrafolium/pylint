# pylint: disable=missing-docstring,too-few-public-methods,no-member,unused-argument, useless-object-inheritance


class NotUselessSuper(object):
    def not_passing_all_params(self, first, *args, second=None, **kwargs):
        return super(NotUselessSuper,
                     self).not_passing_all_params(*args, second, **kwargs)


class UselessSuper(object):

    # [useless-super-delegation]
    def useless(self, first, *, second=None, **kwargs):
        return super(UselessSuper, self).useless(first,
                                                 second=second,
                                                 **kwargs)
