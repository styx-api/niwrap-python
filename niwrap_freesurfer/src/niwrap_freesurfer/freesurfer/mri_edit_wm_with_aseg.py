# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_EDIT_WM_WITH_ASEG_METADATA = Metadata(
    id="dba94a75baa2e8d9087db292cdbd668dccb68ca5.boutiques",
    name="mri_edit_wm_with_aseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriEditWmWithAsegParameters = typing.TypedDict('MriEditWmWithAsegParameters', {
    "__STYX_TYPE__": typing.Literal["mri_edit_wm_with_aseg"],
    "input_wm": InputPathType,
    "input_t1_brain": InputPathType,
    "aseg": InputPathType,
    "output_wm": str,
    "fillven": bool,
    "fix_scm_ha": typing.NotRequired[int | None],
    "fix_scm_ha_only": typing.NotRequired[str | None],
    "keep": bool,
    "keep_in": bool,
    "lh": bool,
    "rh": bool,
    "fix_ento_wm": typing.NotRequired[str | None],
    "sa_fix_ento_wm": typing.NotRequired[str | None],
    "debug_voxel": typing.NotRequired[list[float] | None],
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
        "mri_edit_wm_with_aseg": mri_edit_wm_with_aseg_cargs,
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
        "mri_edit_wm_with_aseg": mri_edit_wm_with_aseg_outputs,
    }.get(t)


class MriEditWmWithAsegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_edit_wm_with_aseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_wm_file: OutputPathType
    """Edited white matter output file"""


def mri_edit_wm_with_aseg_params(
    input_wm: InputPathType,
    input_t1_brain: InputPathType,
    aseg: InputPathType,
    output_wm: str,
    fillven: bool = False,
    fix_scm_ha: int | None = None,
    fix_scm_ha_only: str | None = None,
    keep: bool = False,
    keep_in: bool = False,
    lh: bool = False,
    rh: bool = False,
    fix_ento_wm: str | None = None,
    sa_fix_ento_wm: str | None = None,
    debug_voxel: list[float] | None = None,
) -> MriEditWmWithAsegParameters:
    """
    Build parameters.
    
    Args:
        input_wm: Input white matter file.
        input_t1_brain: Input T1/brain file.
        aseg: Anatomical segmentation file.
        output_wm: Output white matter file.
        fillven: Fill ventricular system.
        fix_scm_ha: Remove voxels in amygdala, ILV, and parts of hippocampus.
        fix_scm_ha_only: Standalone: fix SCM using aseg.presurf.mgz.
        keep: Keep edits as found in output volume.
        keep_in: Keep edits as found in input volume.
        lh: Erase right hemisphere labels from output.
        rh: Erase left hemisphere labels from output.
        fix_ento_wm: Insert lhval rhval where {3,4}006 and {3,4}201 in entowm\
            volume.
        sa_fix_ento_wm: Standalone version of fix ento-WM.
        debug_voxel: Specify a voxel to edit with coordinates Gx Gy Gz.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_edit_wm_with_aseg",
        "input_wm": input_wm,
        "input_t1_brain": input_t1_brain,
        "aseg": aseg,
        "output_wm": output_wm,
        "fillven": fillven,
        "keep": keep,
        "keep_in": keep_in,
        "lh": lh,
        "rh": rh,
    }
    if fix_scm_ha is not None:
        params["fix_scm_ha"] = fix_scm_ha
    if fix_scm_ha_only is not None:
        params["fix_scm_ha_only"] = fix_scm_ha_only
    if fix_ento_wm is not None:
        params["fix_ento_wm"] = fix_ento_wm
    if sa_fix_ento_wm is not None:
        params["sa_fix_ento_wm"] = sa_fix_ento_wm
    if debug_voxel is not None:
        params["debug_voxel"] = debug_voxel
    return params


def mri_edit_wm_with_aseg_cargs(
    params: MriEditWmWithAsegParameters,
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
    cargs.append("mri_edit_wm_with_aseg")
    cargs.append(execution.input_file(params.get("input_wm")))
    cargs.append(execution.input_file(params.get("input_t1_brain")))
    cargs.append(execution.input_file(params.get("aseg")))
    cargs.append(params.get("output_wm"))
    if params.get("fillven"):
        cargs.append("-fillven")
    if params.get("fix_scm_ha") is not None:
        cargs.extend([
            "-fix-scm-ha",
            str(params.get("fix_scm_ha"))
        ])
    if params.get("fix_scm_ha_only") is not None:
        cargs.extend([
            "-fix-scm-ha-only",
            params.get("fix_scm_ha_only")
        ])
    if params.get("keep"):
        cargs.append("-keep")
    if params.get("keep_in"):
        cargs.append("-keep-in")
    if params.get("lh"):
        cargs.append("-lh")
    if params.get("rh"):
        cargs.append("-rh")
    if params.get("fix_ento_wm") is not None:
        cargs.extend([
            "-fix-ento-wm",
            params.get("fix_ento_wm")
        ])
    if params.get("sa_fix_ento_wm") is not None:
        cargs.extend([
            "-sa-fix-ento-wm",
            params.get("sa_fix_ento_wm")
        ])
    if params.get("debug_voxel") is not None:
        cargs.extend([
            "-debug_voxel",
            *map(str, params.get("debug_voxel"))
        ])
    return cargs


def mri_edit_wm_with_aseg_outputs(
    params: MriEditWmWithAsegParameters,
    execution: Execution,
) -> MriEditWmWithAsegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriEditWmWithAsegOutputs(
        root=execution.output_file("."),
        output_wm_file=execution.output_file(params.get("output_wm")),
    )
    return ret


def mri_edit_wm_with_aseg_execute(
    params: MriEditWmWithAsegParameters,
    execution: Execution,
) -> MriEditWmWithAsegOutputs:
    """
    A tool for editing white matter with anatomical segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriEditWmWithAsegOutputs`).
    """
    params = execution.params(params)
    cargs = mri_edit_wm_with_aseg_cargs(params, execution)
    ret = mri_edit_wm_with_aseg_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_edit_wm_with_aseg(
    input_wm: InputPathType,
    input_t1_brain: InputPathType,
    aseg: InputPathType,
    output_wm: str,
    fillven: bool = False,
    fix_scm_ha: int | None = None,
    fix_scm_ha_only: str | None = None,
    keep: bool = False,
    keep_in: bool = False,
    lh: bool = False,
    rh: bool = False,
    fix_ento_wm: str | None = None,
    sa_fix_ento_wm: str | None = None,
    debug_voxel: list[float] | None = None,
    runner: Runner | None = None,
) -> MriEditWmWithAsegOutputs:
    """
    A tool for editing white matter with anatomical segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_wm: Input white matter file.
        input_t1_brain: Input T1/brain file.
        aseg: Anatomical segmentation file.
        output_wm: Output white matter file.
        fillven: Fill ventricular system.
        fix_scm_ha: Remove voxels in amygdala, ILV, and parts of hippocampus.
        fix_scm_ha_only: Standalone: fix SCM using aseg.presurf.mgz.
        keep: Keep edits as found in output volume.
        keep_in: Keep edits as found in input volume.
        lh: Erase right hemisphere labels from output.
        rh: Erase left hemisphere labels from output.
        fix_ento_wm: Insert lhval rhval where {3,4}006 and {3,4}201 in entowm\
            volume.
        sa_fix_ento_wm: Standalone version of fix ento-WM.
        debug_voxel: Specify a voxel to edit with coordinates Gx Gy Gz.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriEditWmWithAsegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EDIT_WM_WITH_ASEG_METADATA)
    params = mri_edit_wm_with_aseg_params(
        input_wm=input_wm,
        input_t1_brain=input_t1_brain,
        aseg=aseg,
        output_wm=output_wm,
        fillven=fillven,
        fix_scm_ha=fix_scm_ha,
        fix_scm_ha_only=fix_scm_ha_only,
        keep=keep,
        keep_in=keep_in,
        lh=lh,
        rh=rh,
        fix_ento_wm=fix_ento_wm,
        sa_fix_ento_wm=sa_fix_ento_wm,
        debug_voxel=debug_voxel,
    )
    return mri_edit_wm_with_aseg_execute(params, execution)


__all__ = [
    "MRI_EDIT_WM_WITH_ASEG_METADATA",
    "MriEditWmWithAsegOutputs",
    "MriEditWmWithAsegParameters",
    "mri_edit_wm_with_aseg",
    "mri_edit_wm_with_aseg_params",
]
