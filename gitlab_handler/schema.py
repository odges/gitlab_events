from typing import Optional

from pydantic import BaseModel

from gitlab_handler.custom_type import ActionType, EventType


class UserAuthorEvent(BaseModel):
    id: int
    name: str
    username: str
    avatar_url: str
    email: str


class ProjectEvent(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    web_url: Optional[str]
    avatar_url: Optional[str]
    git_ssh_url: Optional[str]
    git_http_url: Optional[str]
    namespace: Optional[str]
    visibility_level: int
    path_with_namespace: Optional[str]
    default_branch: Optional[str]
    ci_config_path: Optional[str]
    homepage: Optional[str]
    url: Optional[str]
    ssh_url: Optional[str]
    http_url: Optional[str]


class ObjectEventAttributes(BaseModel):
    attachment: Optional[str]
    author_id: Optional[int]
    commit_id: Optional[str]
    created_at: str
    discussion_id: Optional[str]
    id: int
    line_code: Optional[str]
    note: Optional[str]
    noteable_id: Optional[int]
    noteable_type: Optional[str]
    project_id: Optional[int]
    resolved_at: Optional[str]
    resolved_by_id: Optional[str]
    resolved_by_push: Optional[str]
    st_diff: Optional[str]
    system: Optional[bool]
    type: Optional[str]
    updated_at: Optional[str]
    updated_by_id: Optional[int]
    description: Optional[str]
    url: Optional[str]

    action: Optional[ActionType]

    status: Optional[str]
    ref: Optional[str]


class RepositoryInfo(BaseModel):
    name: str
    url: str
    description: Optional[str]
    homepage: Optional[str]


class MergeRequestObject(BaseModel):
    assignee_id: Optional[int]
    author_id: Optional[int]
    description: Optional[str]
    source_branch: str
    target_branch: str
    title: str
    updated_by_id: Optional[int]
    url: str
    blocking_discussions_resolved: bool


class EventObjectModel(BaseModel):
    object_kind: str
    event_type: Optional[EventType]
    user: UserAuthorEvent
    project_id: Optional[int]
    project: ProjectEvent
    object_attributes: ObjectEventAttributes
    repository: Optional[RepositoryInfo]
    merge_request: Optional[MergeRequestObject]
