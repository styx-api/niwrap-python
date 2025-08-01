# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_CVS_CHECK_METADATA = Metadata(
    id="72ac9d6e08580c333bd915db7bf636a0c1d187a9.boutiques",
    name="mri_cvs_check",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriCvsCheckParameters = typing.TypedDict('MriCvsCheckParameters', {
    "__STYXTYPE__": typing.Literal["mri_cvs_check"],
    "mov_subjid": str,
    "template_subjid": typing.NotRequired[str | None],
    "hemi": typing.NotRequired[typing.Literal["lh", "rh"] | None],
    "help": bool,
    "version": bool,
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
        "mri_cvs_check": mri_cvs_check_cargs,
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


class MriCvsCheckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_cvs_check(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_cvs_check_params(
    mov_subjid: str,
    template_subjid: str | None = None,
    hemi: typing.Literal["lh", "rh"] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MriCvsCheckParameters:
    """
    Build parameters.
    
    Args:
        mov_subjid: Subject id for the subject to be moved/registered (Should\
            be present in SUBJECTS_DIR).
        template_subjid: Subject id for the template subject to be kept fixed.\
            If missing, CVS template is assumed as a target.
        hemi: The hemisphere that is going to be processed. It can be 'lh' or\
            'rh'.
        help_: Print help and exit.
        version: Print version and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_cvs_check",
        "mov_subjid": mov_subjid,
        "help": help_,
        "version": version,
    }
    if template_subjid is not None:
        params["template_subjid"] = template_subjid
    if hemi is not None:
        params["hemi"] = hemi
    return params


def mri_cvs_check_cargs(
    params: MriCvsCheckParameters,
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
    cargs.append("mri_cvs_check")
    cargs.extend([
        "--mov",
        params.get("mov_subjid")
    ])
    if params.get("template_subjid") is not None:
        cargs.extend([
            "--template",
            params.get("template_subjid")
        ])
    if params.get("hemi") is not None:
        cargs.extend([
            "--hemi",
            params.get("hemi")
        ])
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def mri_cvs_check_outputs(
    params: MriCvsCheckParameters,
    execution: Execution,
) -> MriCvsCheckOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCvsCheckOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_cvs_check_execute(
    params: MriCvsCheckParameters,
    execution: Execution,
) -> MriCvsCheckOutputs:
    """
    Checks whether the files required for mri_cvs_register all exist.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCvsCheckOutputs`).
    """
    params = execution.params(params)
    cargs = mri_cvs_check_cargs(params, execution)
    ret = mri_cvs_check_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_cvs_check(
    mov_subjid: str,
    template_subjid: str | None = None,
    hemi: typing.Literal["lh", "rh"] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriCvsCheckOutputs:
    """
    Checks whether the files required for mri_cvs_register all exist.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        mov_subjid: Subject id for the subject to be moved/registered (Should\
            be present in SUBJECTS_DIR).
        template_subjid: Subject id for the template subject to be kept fixed.\
            If missing, CVS template is assumed as a target.
        hemi: The hemisphere that is going to be processed. It can be 'lh' or\
            'rh'.
        help_: Print help and exit.
        version: Print version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCvsCheckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CVS_CHECK_METADATA)
    params = mri_cvs_check_params(
        mov_subjid=mov_subjid,
        template_subjid=template_subjid,
        hemi=hemi,
        help_=help_,
        version=version,
    )
    return mri_cvs_check_execute(params, execution)


__all__ = [
    "MRI_CVS_CHECK_METADATA",
    "MriCvsCheckOutputs",
    "MriCvsCheckParameters",
    "mri_cvs_check",
    "mri_cvs_check_params",
]
