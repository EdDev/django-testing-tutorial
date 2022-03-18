# MIT License
#
# Copyright (c) 2022 Edward Haas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import pytest

from . import models


USERNAME = "ed"
FIRSTNAME = "Edy"
LASTNAME = "Haas"


@pytest.fixture
def member0():
    return models.Member(username=USERNAME, firstname=FIRSTNAME, lastname=LASTNAME)


class TestMemberModel:
    def test_new_member(self, member0):
        assert member0.username == USERNAME
        assert member0.firstname == FIRSTNAME
        assert member0.lastname == LASTNAME

    @pytest.mark.django_db()
    def test_persist_member(self, member0):
        member0.save()

        assert member0 in models.Member.objects.all()


SPEAKER_ROLE_NAME = "speaker"
SPEAKER_ROLE_DESC = "Gives a lecture"


@pytest.fixture
def role0():
    return models.Role(name=SPEAKER_ROLE_NAME, description=SPEAKER_ROLE_DESC)


class TestRoleModel:
    def test_new_role(self, role0):
        assert role0.name == SPEAKER_ROLE_NAME
        assert role0.description == SPEAKER_ROLE_DESC

    @pytest.mark.django_db()
    def test_persist_role(self, role0):
        role0.save()

        assert role0 in models.Role.objects.all()


@pytest.fixture
def member_role0(member0, role0):
    return models.MemberRole(member=member0, role=role0)


@pytest.fixture
def persisted_member_role0(db, member_role0):
    member_role0.member.save()
    member_role0.role.save()
    member_role0.save()
    return member_role0


@pytest.fixture
def persisted_member_role_pool(persisted_member_role0):
    mentor_role = models.Role(name="mentor", description="Mentor students")
    beyond_member = models.Member(username="beyond")

    new_member_role = models.MemberRole(member=beyond_member, role=mentor_role)
    mentor_role.save()
    beyond_member.save()
    new_member_role.save()

    return [persisted_member_role0, new_member_role]


class TestMemberRoleModel:
    def test_new_member_role(self, member_role0):
        assert member_role0.member.username == USERNAME
        assert member_role0.role.name == SPEAKER_ROLE_NAME

    @pytest.mark.django_db()
    def test_persist_member_role(self, member_role0):
        member_role0.member.save()
        member_role0.role.save()
        member_role0.save()

        assert member_role0 in models.MemberRole.objects.all()

    def test_delete_ref_member(self, persisted_member_role0):
        persisted_member_role0.member.delete()

        assert persisted_member_role0 not in models.MemberRole.objects.all()

    def test_delete_ref_role(self, persisted_member_role0):
        persisted_member_role0.role.delete()

        assert persisted_member_role0 not in models.MemberRole.objects.all()

    def test_filter_all(self, persisted_member_role_pool):
        assert persisted_member_role_pool == list(models.MemberRole.filter())

    def test_filter_by_role(self, persisted_member_role_pool):
        expected_filtered_member_role = persisted_member_role_pool[1]
        role2filter = expected_filtered_member_role.role

        assert [expected_filtered_member_role] == list(
            models.MemberRole.filter(role=role2filter)
        )

    def test_filter_by_member(self, persisted_member_role_pool):
        expected_filtered_member_role = persisted_member_role_pool[1]
        member2filter = expected_filtered_member_role.member

        assert [expected_filtered_member_role] == list(
            models.MemberRole.filter(member=member2filter)
        )
