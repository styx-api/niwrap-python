# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

WMEDITS2SURF_METADATA = Metadata(
    id="0c7cb381e9d90786951e70e4d39e8ecbb9e43b31.boutiques",
    name="wmedits2surf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Wmedits2surfParameters = typing.TypedDict('Wmedits2surfParameters', {
    "__STYX_TYPE__": typing.Literal["wmedits2surf"],
    "subject": str,
    "self": bool,
    "overwrite": bool,
    "tmp_dir": typing.NotRequired[str | None],
    "cleanup": bool,
    "no_cleanup": bool,
    "debug": bool,
    "lh": bool,
    "rh": bool,
    "no_surfs": bool,
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
        "wmedits2surf": wmedits2surf_cargs,
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
        "wmedits2surf": wmedits2surf_outputs,
    }.get(t)


class Wmedits2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `wmedits2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    lh_wmerase: OutputPathType
    """Left hemisphere white matter erase surface file."""
    rh_wmerase: OutputPathType
    """Right hemisphere white matter erase surface file."""
    lh_wmfill: OutputPathType
    """Left hemisphere white matter fill surface file."""
    rh_wmfill: OutputPathType
    """Right hemisphere white matter fill surface file."""
    wm_erase_stats: OutputPathType
    """Statistics on the number of voxels erased."""
    wm_fill_stats: OutputPathType
    """Statistics on the number of voxels filled."""


def wmedits2surf_params(
    subject: str,
    self: bool = False,
    overwrite: bool = False,
    tmp_dir: str | None = None,
    cleanup: bool = False,
    no_cleanup: bool = False,
    debug: bool = False,
    lh: bool = False,
    rh: bool = False,
    no_surfs: bool = False,
) -> Wmedits2surfParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier.
        overwrite: Force overwriting of existing results.
        tmp_dir: Temporary directory.
        cleanup: Cleanup temporary files after execution.
        no_cleanup: Do not cleanup temporary files after execution.
        debug: Debug mode.
        lh: Only do left hemisphere.
        rh: Only do right hemisphere.
        no_surfs: Do not compute surfaces, only count stats.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "wmedits2surf",
        "subject": subject,
        "self": self,
        "overwrite": overwrite,
        "cleanup": cleanup,
        "no_cleanup": no_cleanup,
        "debug": debug,
        "lh": lh,
        "rh": rh,
        "no_surfs": no_surfs,
    }
    if tmp_dir is not None:
        params["tmp_dir"] = tmp_dir
    return params


def wmedits2surf_cargs(
    params: Wmedits2surfParameters,
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
    cargs.append("wmedits2surf")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    if params.get("self"):
        cargs.append("--self")
    if params.get("overwrite"):
        cargs.append("--overwrite")
    if params.get("tmp_dir") is not None:
        cargs.extend([
            "--tmp",
            params.get("tmp_dir")
        ])
    if params.get("cleanup"):
        cargs.append("--cleanup")
    if params.get("no_cleanup"):
        cargs.append("--no-cleanup")
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("lh"):
        cargs.append("--lh")
    if params.get("rh"):
        cargs.append("--rh")
    if params.get("no_surfs"):
        cargs.append("--no-surfs")
    return cargs


def wmedits2surf_outputs(
    params: Wmedits2surfParameters,
    execution: Execution,
) -> Wmedits2surfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Wmedits2surfOutputs(
        root=execution.output_file("."),
        lh_wmerase=execution.output_file("subject/surf/lh.wmerase.fsa.mgh"),
        rh_wmerase=execution.output_file("subject/surf/rh.wmerase.fsa.mgh"),
        lh_wmfill=execution.output_file("subject/surf/lh.wmfill.fsa.mgh"),
        rh_wmfill=execution.output_file("subject/surf/rh.wmfill.fsa.mgh"),
        wm_erase_stats=execution.output_file("subject/stats/wm.erase.dat"),
        wm_fill_stats=execution.output_file("subject/stats/wm.fill.dat"),
    )
    return ret


def wmedits2surf_execute(
    params: Wmedits2surfParameters,
    execution: Execution,
) -> Wmedits2surfOutputs:
    """
    Computes binary maps of surface locations where the wm.mgz has been edited.
    Creates files for each hemisphere for each type of edit.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Wmedits2surfOutputs`).
    """
    params = execution.params(params)
    cargs = wmedits2surf_cargs(params, execution)
    ret = wmedits2surf_outputs(params, execution)
    execution.run(cargs)
    return ret


def wmedits2surf(
    subject: str,
    self: bool = False,
    overwrite: bool = False,
    tmp_dir: str | None = None,
    cleanup: bool = False,
    no_cleanup: bool = False,
    debug: bool = False,
    lh: bool = False,
    rh: bool = False,
    no_surfs: bool = False,
    runner: Runner | None = None,
) -> Wmedits2surfOutputs:
    """
    Computes binary maps of surface locations where the wm.mgz has been edited.
    Creates files for each hemisphere for each type of edit.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        overwrite: Force overwriting of existing results.
        tmp_dir: Temporary directory.
        cleanup: Cleanup temporary files after execution.
        no_cleanup: Do not cleanup temporary files after execution.
        debug: Debug mode.
        lh: Only do left hemisphere.
        rh: Only do right hemisphere.
        no_surfs: Do not compute surfaces, only count stats.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Wmedits2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WMEDITS2SURF_METADATA)
    params = wmedits2surf_params(
        subject=subject,
        self=self,
        overwrite=overwrite,
        tmp_dir=tmp_dir,
        cleanup=cleanup,
        no_cleanup=no_cleanup,
        debug=debug,
        lh=lh,
        rh=rh,
        no_surfs=no_surfs,
    )
    return wmedits2surf_execute(params, execution)


__all__ = [
    "WMEDITS2SURF_METADATA",
    "Wmedits2surfOutputs",
    "Wmedits2surfParameters",
    "wmedits2surf",
    "wmedits2surf_params",
]
