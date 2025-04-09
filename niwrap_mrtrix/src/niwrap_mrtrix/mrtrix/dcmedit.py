# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DCMEDIT_METADATA = Metadata(
    id="8cde5cf6f19725e4d438d7089e7f5a9e71f0b93d.boutiques",
    name="dcmedit",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


DcmeditTagParameters = typing.TypedDict('DcmeditTagParameters', {
    "__STYX_TYPE__": typing.Literal["tag"],
    "group": str,
    "element": str,
    "newvalue": str,
})


DcmeditConfigParameters = typing.TypedDict('DcmeditConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


DcmeditParameters = typing.TypedDict('DcmeditParameters', {
    "__STYX_TYPE__": typing.Literal["dcmedit"],
    "anonymise": bool,
    "id": typing.NotRequired[str | None],
    "tag": typing.NotRequired[list[DcmeditTagParameters] | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[DcmeditConfigParameters] | None],
    "help": bool,
    "version": bool,
    "file": InputPathType,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "dcmedit": dcmedit_cargs,
        "tag": dcmedit_tag_cargs,
        "config": dcmedit_config_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


def dcmedit_tag_params(
    group: str,
    element: str,
    newvalue: str,
) -> DcmeditTagParameters:
    """
    Build parameters.
    
    Args:
        group: replace specific tag.
        element: replace specific tag.
        newvalue: replace specific tag.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tag",
        "group": group,
        "element": element,
        "newvalue": newvalue,
    }
    return params


def dcmedit_tag_cargs(
    params: DcmeditTagParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-tag")
    cargs.append(params.get("group"))
    cargs.append(params.get("element"))
    cargs.append(params.get("newvalue"))
    return cargs


def dcmedit_config_params(
    key: str,
    value: str,
) -> DcmeditConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def dcmedit_config_cargs(
    params: DcmeditConfigParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class DcmeditOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcmedit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dcmedit_params(
    file: InputPathType,
    anonymise: bool = False,
    id_: str | None = None,
    tag: list[DcmeditTagParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DcmeditConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> DcmeditParameters:
    """
    Build parameters.
    
    Args:
        file: the DICOM file to be edited.
        anonymise: remove any identifiable information, by replacing the\
            following tags:\
            - any tag with Value Representation PN will be replaced with\
            'anonymous'\
            - tag (0010,0030) PatientBirthDate will be replaced with an empty\
            string\
            WARNING: there is no guarantee that this command will remove all\
            identiable information, since such information may be contained in\
            any number of private vendor-specific tags. You will need to\
            double-check the results independently if you need to ensure\
            anonymity.
        id_: replace all ID tags with string supplied. This consists of tags\
            (0010, 0020) PatientID and (0010, 1000) OtherPatientIDs.
        tag: replace specific tag.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dcmedit",
        "anonymise": anonymise,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "file": file,
    }
    if id_ is not None:
        params["id"] = id_
    if tag is not None:
        params["tag"] = tag
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def dcmedit_cargs(
    params: DcmeditParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("dcmedit")
    if params.get("anonymise"):
        cargs.append("-anonymise")
    if params.get("id") is not None:
        cargs.extend([
            "-id",
            params.get("id")
        ])
    if params.get("tag") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("tag")] for a in c])
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(execution.input_file(params.get("file")))
    return cargs


def dcmedit_outputs(
    params: DcmeditParameters,
    execution: Execution,
) -> DcmeditOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DcmeditOutputs(
        root=execution.output_file("."),
    )
    return ret


def dcmedit_execute(
    params: DcmeditParameters,
    execution: Execution,
) -> DcmeditOutputs:
    """
    Edit DICOM file in-place.
    
    Note that this command simply replaces the existing values without modifying
    the DICOM structure in any way. Replacement text will be truncated if it is
    too long to fit inside the existing tag.
    
    WARNING: this command will modify existing data! It is recommended to run
    this command on a copy of the original data set to avoid loss of data.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DcmeditOutputs`).
    """
    params = execution.params(params)
    cargs = dcmedit_cargs(params, execution)
    ret = dcmedit_outputs(params, execution)
    execution.run(cargs)
    return ret


def dcmedit(
    file: InputPathType,
    anonymise: bool = False,
    id_: str | None = None,
    tag: list[DcmeditTagParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DcmeditConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> DcmeditOutputs:
    """
    Edit DICOM file in-place.
    
    Note that this command simply replaces the existing values without modifying
    the DICOM structure in any way. Replacement text will be truncated if it is
    too long to fit inside the existing tag.
    
    WARNING: this command will modify existing data! It is recommended to run
    this command on a copy of the original data set to avoid loss of data.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        file: the DICOM file to be edited.
        anonymise: remove any identifiable information, by replacing the\
            following tags:\
            - any tag with Value Representation PN will be replaced with\
            'anonymous'\
            - tag (0010,0030) PatientBirthDate will be replaced with an empty\
            string\
            WARNING: there is no guarantee that this command will remove all\
            identiable information, since such information may be contained in\
            any number of private vendor-specific tags. You will need to\
            double-check the results independently if you need to ensure\
            anonymity.
        id_: replace all ID tags with string supplied. This consists of tags\
            (0010, 0020) PatientID and (0010, 1000) OtherPatientIDs.
        tag: replace specific tag.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DcmeditOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMEDIT_METADATA)
    params = dcmedit_params(
        anonymise=anonymise,
        id_=id_,
        tag=tag,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        file=file,
    )
    return dcmedit_execute(params, execution)


__all__ = [
    "DCMEDIT_METADATA",
    "DcmeditConfigParameters",
    "DcmeditOutputs",
    "DcmeditParameters",
    "DcmeditTagParameters",
    "dcmedit",
    "dcmedit_config_params",
    "dcmedit_params",
    "dcmedit_tag_params",
]
